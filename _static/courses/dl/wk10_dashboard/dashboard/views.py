import json
import time
import torch
import torch.nn as nn
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def train(request):
    def event_stream():
        # XOR data
        X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float32)
        y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float32)

        # Model
        model = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

        criterion = nn.BCELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

        # Send initial scatter data
        scatter = []
        for i in range(4):
            scatter.append({
                'x': X[i][0].item(),
                'y': X[i][1].item(),
                'label': int(y[i].item())
            })
        yield f"data: {json.dumps({'type': 'scatter', 'data': scatter})}\n\n"

        # Training loop
        for epoch in range(201):
            y_hat = model(X)
            loss = criterion(y_hat, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Get predictions for visualization
            with torch.no_grad():
                pred = model(X).squeeze().tolist()

            # Get decision boundary points
            grid = []
            for gx in range(21):
                for gy in range(21):
                    px = gx / 20.0
                    py = gy / 20.0
                    inp = torch.tensor([[px, py]], dtype=torch.float32)
                    with torch.no_grad():
                        pv = model(inp).item()
                    grid.append({'x': px, 'y': py, 'v': pv})

            yield f"data: {json.dumps({'type': 'update', 'epoch': epoch, 'loss': loss.item(), 'pred': pred, 'grid': grid})}\n\n"
            time.sleep(0.02)

        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    return response
