"""
wk09-hw.py — เฉลยการบ้านสัปดาห์ที่ 9 (1145208 การเรียนรู้เชิงลึก)

รันด้วย:  uv run wk09-hw.py
ต้องติดตั้ง:  uv add torch matplotlib

ข้อ 1  เปลี่ยน learning rate เป็น 0.001 และ 1.0 — เกิดอะไรขึ้น?
ข้อ 2  ข้อมูล XOR กับเพอร์เซปตรอนเส้นตรงเดียว — fail อย่างไร?
ข้อ 3  (ท้าทาย) เพิ่ม hidden layer: Linear(2,4) -> ReLU -> Linear(4,1) แก้ XOR
"""

import torch

torch.manual_seed(42)


# ---------- ข้อมูล ----------
def make_linear_data(n=200):
    """ข้อมูลที่แบ่งด้วยเส้นตรงได้ (เหมือนในคาบเรียน)"""
    X = torch.randn(n, 2)
    y = ((X[:, 0] * 1.5 + X[:, 1] - 0.5) > 0).float().unsqueeze(1)
    return X, y


def make_xor_data(n=200):
    """ข้อมูล XOR: จุดในช่องที่ 1,3 = class 1, ช่องที่ 2,4 = class 0
    (คลาสสองฝั่งทแยงกัน — เส้นตรงเส้นเดียวแบ่งไม่ได้แน่นอน)"""
    X = torch.rand(n, 2) * 4 - 2  # สุ่มในช่วง [-2, 2]
    y = (X[:, 0] * X[:, 1] > 0).float().unsqueeze(1)
    return X, y


# ---------- โมเดล ----------
def build_perceptron():
    # ŷ = σ(w·x + b)  — ตัวแบ่งเป็นได้แค่ "เส้นตรงเส้นเดียว"
    return torch.nn.Sequential(
        torch.nn.Linear(2, 1),
        torch.nn.Sigmoid(),
    )


def build_mlp():
    # ข้อ 3: hidden layer ทำให้ตัดสินใจได้มากกว่าเส้นตรง
    return torch.nn.Sequential(
        torch.nn.Linear(2, 4),
        torch.nn.ReLU(),
        torch.nn.Linear(4, 1),
        torch.nn.Sigmoid(),
    )


# ---------- การเทรนและการวัด ----------
def train(model, X, y, lr, epochs=300):
    loss_fn = torch.nn.BCELoss()
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    for epoch in range(epochs):
        y_hat = model(X)
        loss = loss_fn(y_hat, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
    return loss.item()


def accuracy(model, X, y):
    with torch.no_grad():
        return ((model(X) > 0.5).float() == y).float().mean().item()


# ---------- ข้อ 1: ทดลอง learning rate ----------
print("=" * 62)
print("ข้อ 1: ผลของ learning rate (ข้อมูลเส้นตรง, 300 epoch)")
print("=" * 62)
X, y = make_linear_data()
for lr in (0.001, 0.1, 1.0):
    torch.manual_seed(42)  # ค่าเริ่มต้น w, b เหมือนกันทุกครั้ง
    model = build_perceptron()
    final_loss = train(model, X, y, lr)
    print(f"  lr = {lr:<6} | final loss = {final_loss:8.4f} "
          f"| acc = {accuracy(model, X, y):6.1%}")
print("""
  สรุป: lr = 0.001 ก้าวเล็กเกินไป -> ครบ 300 epoch แล้ว loss ยังสูง (0.44)
                   เพราะเดินทีละเซนติเมตร ยังไม่ถึงที่หมาย
        lr = 0.1   กำลังดี -> loss ลดลงเป็นระบบ จน 99%
        lr = 1.0   โจทย์นี้ง่ายมาก (สองกลุ่มแยกกันชัด) เส้นใหญ่เลยรอด
                   แต่อย่าเข้าใจว่าก้าวใหญ่ปลอดภัย — โจทย์ง่ายซ่อนปัญหา
                   พอโจทย์จริงยากขึ้น (ข้อมูลทับกัน/โมเดลใหญ่) lr ใหญ่จะ
                   ทำ loss แกว่งไปมาหรือระเบิดเป็น NaN ทันที
""")

# ---------- ข้อ 2: เพอร์เซปตรอน vs XOR ----------
print("=" * 62)
print("ข้อ 2: เพอร์เซปตรอน (เส้นตรงเดียว) กับข้อมูล XOR")
print("=" * 62)
X_xor, y_xor = make_xor_data()
torch.manual_seed(42)
model = build_perceptron()
loss = train(model, X_xor, y_xor, lr=0.1)
print(f"  final loss = {loss:.4f} | acc = {accuracy(model, X_xor, y_xor):6.1%}")
print(f"  คำตอบโง่สุด ๆ (ทายตามจำนวน class ที่เยอะกว่า) = "
      f"{max(y_xor.mean().item(), 1 - y_xor.mean().item()):6.1%}")
print("""
  สรุป: ไม่ว่าจะวางเส้นตรงยังไง ก็แบ่งมุมทแยงสองฝั่งไม่ได้
        เพราะ XOR ไม่ linearly separable -> เพอร์เซปตรอนติดตรงนี้เสมอ
        (Minsky & Papert 1969 คือหลักฐานที่ทำให้ยุค AI หนาวเหน็บ!)
""")

# ---------- ข้อ 3: MLP แก้ XOR ----------
print("=" * 62)
print("ข้อ 3 (ท้าทาย): เพิ่ม hidden layer แล้วแก้ XOR")
print("=" * 62)
torch.manual_seed(42)
mlp = build_mlp()
loss = train(mlp, X_xor, y_xor, lr=0.1, epochs=1000)
print(f"  final loss = {loss:.4f} | acc = {accuracy(mlp, X_xor, y_xor):6.1%}")
print("""
  สรุป: hidden layer 4 นิวรอน + ReLU พับพื้นที่ให้ XOR กลายเป็น
        แบ่งได้ด้วยเส้นตรงในพื้นที่ใหม่ -> acc ต่ำ ๆ กลายเป็น ~100%
""")

# บันทึกภาพเขตการตัดสินใจของ MLP ประกอบคำตอบ
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

xs = torch.linspace(-2.4, 2.4, 200)
xx, yy = torch.meshgrid(xs, xs, indexing="xy")
grid = torch.stack([xx.ravel(), yy.ravel()], dim=1)
with torch.no_grad():
    zz = mlp(grid).reshape(xx.shape)

plt.contourf(xx.numpy(), yy.numpy(), zz.numpy(),
             levels=20, cmap="bwr", alpha=0.6)
plt.colorbar(label="P(class 1)")
Xp, yp = X_xor.numpy(), y_xor.numpy().ravel()
plt.scatter(Xp[yp == 1, 0], Xp[yp == 1, 1],
            c="tab:green", s=15, edgecolors="k", label="class 1")
plt.scatter(Xp[yp == 0, 0], Xp[yp == 0, 1],
            c="tab:red", s=15, edgecolors="k", label="class 0")
plt.legend()
plt.title("Q3: MLP learns the XOR boundary")
plt.savefig("wk09-hw-xor-boundary.png", dpi=120)
print("บันทึกภาพ: wk09-hw-xor-boundary.png")
