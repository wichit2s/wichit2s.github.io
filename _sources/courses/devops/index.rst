.. image:: images/devops-banner.png

DevOps
=============================================================

หลักการ แนวปฏิบัติ และเครื่องมือของ DevOps ปรัชญาของ DevOps กระบวนการอัตโนมัติ และเทคโนโลยีที่เกี่ยวข้อง วงจรการส่งมอบซอฟต์แวร์ การควบคุมเวอร์ชัน การทดสอบอัตโนมัติ Pipelines, Containerization และ Orchestration, แพลตฟอร์มคลาวด์, Infrastructure as Code เครื่องมือสำหรับการเฝ้าระวังและบันทึกข้อมูล


ผลลัพธ์การเรียนรู้
--------------------------
1. ทำความเข้าใจหลักการและวัฒนธรรมหลักของ DevOps
2. ประยุกต์ใช้กลยุทธ์การควบคุมเวอร์ชันสำหรับการพัฒนาร่วมกัน
3. ออกแบบและสร้าง CI/CD Pipelines ที่แข็งแกร่งสำหรับการส่งมอบซอฟต์แวร์อัตโนมัติ
4. บรรจุรวม ปรับใช้และจัดการแอปพลิเคชันที่ใช้ Container ด้วยเครื่องมือ Orchestration 
5. ประยุกต์ใช้หลักการ Infrastructure as Code (IaC) เพื่อจัดเตรียมและจัดการโครงสร้างพื้นฐาน


แผนการสอนรายสัปดาห์ (15 สัปดาห์)
------------------------------------

.. warning:
   เพิ่มลไลด์รายสัปดาห์

.. role:: raw-html(raw)
   :format: html

.. default-role:: raw-html

.. list-table:: ร่างแผนการสอนรายสัปดาห์: หลักการและการปฏิบัติงาน DevOps
   :widths: 10 45 45
   :header-rows: 1

   * - สัปดาห์ที่
     - บรรยาย (1 ชั่วโมง)
     - ปฏิบัติการ (2 ชั่วโมง)
   * - **สัปดาห์ที่ 1**

       * `slides <../../_static/courses/devops/slides/wk01.html>`_
     - **บทนำสู่ DevOps และวัฒนธรรม (Introduction to DevOps & Culture)**

       * DevOps คืออะไร? ความหมาย, ที่มา, ประโยชน์
       * เปรียบเทียบกับโมเดลการพัฒนาแบบเดิม (Waterfall, Agile)
       * แนวคิดหลัก: วัฒนธรรม (Culture), ระบบอัตโนมัติ (Automation), Lean, การวัดผล (Measurement), การแบ่งปัน (Sharing) - CALMS
       * ความสำคัญของการทำงานร่วมกันและการสื่อสาร
       * ภาพรวมเครื่องมือที่จะใช้ในหลักสูตร
     - **ตั้งค่าสภาพแวดล้อมและ Git พื้นฐาน**

       * ติดตั้ง Git, VS Code
       * ทดลองใช้คำสั่ง Git พื้นฐาน (init, add, commit, status) ใน local repository
   * - **สัปดาห์ที่ 2**
     - **การควบคุมเวอร์ชันด้วย Git (Version Control with Git)**

       * แนวคิดของ Version Control System (VCS)
       * Git คืออะไร? ข้อดีและสถาปัตยกรรม
       * Git Commands ที่สำคัญ: clone, push, pull, branch, merge
       * แนวคิดของ Remote Repository (GitHub/GitLab/Gitea - เน้นใช้ GitHub Desktop หรือ CLI)
     - **ฝึกฝน Git และ GitHub**

       * สร้างบัญชี GitHub (ถ้ายังไม่มี)
       * สร้าง Remote Repository บน GitHub
       * ฝึก clone, push, pull, branch, merge ในโปรเจกต์กลุ่มเล็กๆ
       * แก้ไข Conflict เบื้องต้น
   * - **สัปดาห์ที่ 3**
     - **บทนำสู่ Containerization ด้วย Docker (Introduction to Containerization with Docker)**

       * Containerization คืออะไร? ทำไมต้องใช้?
       * เปรียบเทียบกับ Virtual Machine
       * Docker: สถาปัตยกรรม (Daemon, Client, Image, Container, Registry)
       * Docker Commands พื้นฐาน (pull, run, ps, stop, rm, rmi)
       * แนวคิดของ Dockerfile
     - **ติดตั้ง Docker และทดลองใช้งาน**

       * ติดตั้ง Docker Desktop บนคอมพิวเตอร์ส่วนตัว
       * ทดลอง pull และ run Docker Images ยอดนิยม (เช่น Nginx, Ubuntu)
       * ฝึกสร้าง Dockerfile อย่างง่ายสำหรับแอปพลิเคชัน Node.js/Python (Hello World)
       * Build และ Run Docker Image ของตัวเอง
   * - **สัปดาห์ที่ 4**
     - **การจัดการ Docker Images และ Volumes (Docker Images & Volumes Management)**

       * การจัดการ Docker Images (Layers, Caching)
       * Docker Hub และการ Public/Private Repository
       * การทำงานกับ Docker Volumes (Persistent Data)
       * Docker Networks เบื้องต้น
     - **สร้าง Dockerfile ที่ซับซ้อนขึ้นและ Volume**

       * สร้าง Dockerfile ที่ซับซ้อนขึ้น (เช่น ติดตั้ง dependencies เพิ่มเติม)
       * Push Docker Image ของตัวเองขึ้น Docker Hub
       * ทดลอง Mount Volume เพื่อเก็บข้อมูลของ Container
       * เชื่อมต่อ 2 Containers ด้วย Docker Network
   * - **สัปดาห์ที่ 5**
     - **การประกอบแอปพลิเคชันด้วย Docker Compose (Application Assembly with Docker Compose)**

       * ปัญหาของการรันหลาย Containers ด้วยมือ
       * Docker Compose คืออะไร? โครงสร้างไฟล์ :code:`docker-compose.yml`
       * คำสั่ง Docker Compose (up, down, ps, logs)
       * การจัดการ Services, Networks, Volumes ใน Compose
     - **สร้าง Multi-container Application ด้วย Compose**

       * สร้างไฟล์ :code:`docker-compose.yml` สำหรับแอปพลิเคชัน (Web server, Backend, Database)
       * ทดลอง :code:`docker-compose up` และ :code:`down`
       * เชื่อมต่อแอปพลิเคชันทั้งหมดเข้าด้วยกัน
   * - **สัปดาห์ที่ 6**
     - **บทนำสู่ Continuous Integration (CI) (Introduction to Continuous Integration)**

       * CI คืออะไร? ประโยชน์และแนวปฏิบัติ
       * ขั้นตอนหลักของ CI: Build, Test, Static Analysis
       * เครื่องมือ CI (Jenkins, GitLab CI/CD, GitHub Actions - เน้นแนวคิด)
       * การใช้ Git Hooks เพื่อเริ่มกระบวนการ CI
     - **สร้าง CI Pipeline ด้วย GitHub Actions**

       * แนะนำการใช้ GitHub Actions:
       * สร้าง Workflow :code:`.github/workflows/main.yml` อย่างง่าย
       * ตั้งค่าให้รันเมื่อ push โค้ด
       * รัน Linting (ESLint, Pylint) และ Unit Tests สำหรับโปรเจกต์ Hello World
   * - **สัปดาห์ที่ 7**
     - **Continuous Delivery (CD) และ Deployment (CD & Deployment)**

       * CD คืออะไร? เปรียบเทียบกับ Continuous Deployment
       * แนวคิดของการ Deployment Strategies (Blue/Green, Canary, Rolling)
       * ความสำคัญของ Artefact Management
       * การทำ Release Management
     - **ขยาย GitHub Actions สู่ CD**

       * สร้าง Workflow ให้ Build Docker Image หลังผ่าน CI
       * Push Docker Image ไปยัง Docker Hub
       * *จำลอง* การ Deploy ไปยัง Server ด้วย SSH (ใช้ :code:`sshpass` หรือ :code:`scp` เพื่อส่งไฟล์ Docker Compose ไปรันบน VM/Local Machine อื่น)
   * - **สัปดาห์ที่ 8**
     - **Infrastructure as Code (IaC) ด้วย Ansible (IaC with Ansible)**

       * IaC คืออะไร? ทำไมต้องใช้?
       * เปรียบเทียบ Imperative vs. Declarative
       * แนะนำ Ansible: สถาปัตยกรรม (Control Node, Managed Node, Inventory, Playbook, Module)
       * YAML syntax สำหรับ Ansible Playbook
     - **ติดตั้งและใช้งาน Ansible พื้นฐาน**

       * ติดตั้ง Ansible บนคอมพิวเตอร์ส่วนตัว
       * สร้าง Inventory File
       * เขียน Ansible Playbook อย่างง่ายเพื่อ: ติดตั้ง Package (เช่น Nginx), Copy ไฟล์, สตาร์ท Service บนเครื่องเป้าหมาย (อาจใช้ VM บน VirtualBox/WSL2/อีกเครื่องใน LAN)
   * - **สัปดาห์ที่ 9**
     - **การจัดการ Configuration ด้วย Ansible (Configuration Management with Ansible)**

       * Ansible Roles คืออะไร? โครงสร้างและการใช้งาน
       * Ansible Vault สำหรับการจัดการ Sensitive Data
       * การใช้ Variables และ Templates (Jinja2) ใน Playbook
       * การทำ Idempotency
     - **สร้าง Ansible Roles และใช้ Vault**

       * สร้าง Ansible Role สำหรับติดตั้งและตั้งค่า Nginx ให้รัน Web application
       * ใช้ Jinja2 Template เพื่อสร้างไฟล์ configuration ของ Nginx
       * ทดลองใช้ Ansible Vault เพื่อเก็บรหัสผ่าน (จำลอง)
   * - **สัปดาห์ที่ 10**
     - **บทนำสู่ Container Orchestration ด้วย Kubernetes (Introduction to Container Orchestration with Kubernetes)**

       * ปัญหาของการจัดการ Docker Compose ใน Production
       * Kubernetes คืออะไร? (K8s) สถาปัตยกรรม (Master Node, Worker Node, Kubelet, Kube-proxy)
       * Components หลัก: Pods, Deployments, Services, Namespaces
       * YAML syntax สำหรับ Kubernetes Manifests
     - **ติดตั้ง Minikube/K3s และ Deploy Pod**

       * ติดตั้ง Minikube หรือ K3s (lightweight Kubernetes) บนคอมพิวเตอร์ส่วนตัว
       * ทดลองใช้ :code:`kubectl` CLI เพื่อตรวจสอบ Cluster
       * สร้างและ Deploy Pod อย่างง่าย (เช่น Nginx)
       * สร้าง Service เพื่อ Expose Pod
   * - **สัปดาห์ที่ 11**
     - **การจัดการ Kubernetes Workloads (Kubernetes Workload Management)**

       * Deployments: การจัดการ Rollout, Rollback
       * ReplicaSets: การรักษาสถานะของ Pods
       * Horizontal Pod Autoscaler (HPA)
       * Ingress: การจัดการ Traffic ภายนอกเข้าสู่ Cluster
       * ConfigMaps และ Secrets
     - **Deployments, Ingress และ ConfigMaps ใน K8s**

       * สร้าง Deployment สำหรับ Web application (จาก Docker Image ที่สร้างไว้)
       * ทดลอง Scale Deployment
       * สร้าง Ingress เพื่อเข้าถึง Web application จากภายนอก Minikube
       * ใช้ ConfigMaps เพื่อจัดการ Environment Variables
   * - **สัปดาห์ที่ 12**
     - **การเฝ้าระวังและการบันทึกข้อมูล (Monitoring & Logging)**

       * ความสำคัญของการเฝ้าระวัง (Monitoring) และบันทึกข้อมูล (Logging) ใน DevOps
       * Metrics, Logs, Traces (Observability)
       * เครื่องมือยอดนิยม: Prometheus (Metrics), Grafana (Visualization), ELK Stack (Elasticsearch, Logstash, Kibana - Logging)
       * การตั้งค่า Alerting
     - **ติดตั้ง Prometheus และ Grafana**

       * ติดตั้ง Prometheus และ Grafana ด้วย Docker Compose หรือ Minikube Addon
       * ตั้งค่า Prometheus ให้ Scrape Metrics จาก Node (เช่น cAdvisor สำหรับ Docker)
       * สร้าง Dashboard อย่างง่ายใน Grafana เพื่อแสดง Metrics
   * - **สัปดาห์ที่ 13**
     - **Advanced Monitoring & Troubleshooting (การเฝ้าระวังขั้นสูงและการแก้ไขปัญหา)**

       * การใช้ Exported เพื่อเก็บ Metrics จาก Application (Node Exporter, Blackbox Exporter)
       * แนวคิดของ SLOs, SLIs, Error Budgets
       * พื้นฐานการแก้ไขปัญหาในระบบ DevOps (การดู Logs, Metrics, Debugging)
       * Post-mortem Analysis
     - **ตั้งค่า Alerting และฝึก Troubleshooting**

       * สร้าง Alerting Rule ใน Prometheus/Grafana
       * จำลองการเกิดปัญหา (เช่น CPU usage สูง) และดูการทำงานของ Alert
       * ทดลองใช้ :code:`kubectl logs` และ :code:`kubectl describe` สำหรับการ Troubleshooting Kubernetes Pods
   * - **สัปดาห์ที่ 14**
     - **Security ใน DevOps (DevSecOps) และ Best Practices**

       * แนวคิดของ DevSecOps: Shift-Left Security
       * ความปลอดภัยใน Pipeline (SAST, DAST)
       * ความปลอดภัยของ Container (Image Scanning, Runtime Security)
       * ความปลอดภัยของ Configuration (Secrets Management)
       * DevOps Best Practices และ Anti-patterns
     - **Image Scanning และการอภิปรายความปลอดภัย**

       * แนะนำเครื่องมือสแกน Docker Image (เช่น Trivy หรือ Docker Scout ใน Docker Desktop)
       * ทดลองสแกน Docker Image ที่สร้างไว้ และวิเคราะห์ผลลัพธ์
       * อภิปรายและสรุปแนวทางปฏิบัติที่ดีด้านความปลอดภัย
   * - **สัปดาห์ที่ 15**
     - **สรุปและโครงงานกลุ่ม/นำเสนอ (Course Wrap-up & Project Presentation)**

       * สรุปภาพรวมของ DevOps ตั้งแต่ต้นจนจบ
       * แนวโน้มและอนาคตของ DevOps
       * คำแนะนำสำหรับการทำงานในสายอาชีพ DevOps
     - **นำเสนอโครงงานและอภิปราย**

       * นำเสนอโครงงานกลุ่มเล็กๆ (ถ้ามี) หรืออภิปรายกรณีศึกษา
       * ตอบคำถามและให้คำแนะนำเพิ่มเติม


สัดส่วนการประเมินผล
----------------------
- การมีส่วนร่วมในชั้นเรียน: 5%
- งานบ้านและแบบฝึกหัด: 45%
- โครงงานรายวิชา: 30%
- การนำเสนอและรายงาน: 20%


.. role:: raw-html(raw)
   :format: html

.. default-role:: raw-html

.. list-table:: เอกสารประกอบการเรียนรู้ (Learning Resources)
   :widths: 20 20 60
   :header-rows: 1

   * - หัวข้อหลัก
     - แหล่งข้อมูล / เอกสาร
     - คำอธิบายและลิงก์
   * - **1. Git และ Version Control**
     - Pro Git Book (Online Version)
     - :raw-html:`<p>หนังสือ Pro Git เป็นแหล่งข้อมูลที่ครอบคลุมและละเอียดที่สุดเกี่ยวกับ Git ตั้งแต่พื้นฐานไปจนถึงขั้นสูง มีให้อ่านฟรีออนไลน์ เป็นภาษาอังกฤษ</p><p><b>ลิงก์:</b> <a href="https://git-scm.com/book/en/v2">https://git-scm.com/book/en/v2</a></p>`
   * -
     - GitHub Docs
     - :raw-html:`<p>เอกสารอย่างเป็นทางการของ GitHub ที่สอนวิธีการใช้งาน GitHub ตั้งแต่การสร้าง Repository, การ Pull Request ไปจนถึงฟีเจอร์อื่นๆ ที่เกี่ยวข้องกับการทำงานร่วมกัน</p><p><b>ลิงก์:</b> <a href="https://docs.github.com/">https://docs.github.com/</a></p>`
   * -
     - Git Cheat Sheet (PDF)
     - :raw-html:`<p>สรุปคำสั่ง Git ที่ใช้งานบ่อยๆ พิมพ์ออกมาแปะไว้ข้างโต๊ะได้เลย</p><p><b>ลิงก์:</b> <a href="https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf">https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf</a></p>`
   * - **2. Docker และ Containerization**
     - Docker Documentation
     - :raw-html:`<p>เอกสารทางการจาก Docker เป็นแหล่งข้อมูลที่ดีที่สุดในการเรียนรู้ Docker ทั้งแนวคิด, การใช้งาน Docker CLI, Dockerfile และ Docker Compose</p><p><b>ลิงก์:</b> <a href="https://docs.docker.com/">https://docs.docker.com/</a></p>`
   * -
     - Play with Docker Classroom
     - :raw-html:`<p>แพลตฟอร์มแบบอินเทอร์แอคทีฟที่ให้คุณทดลองใช้ Docker ในเบราว์เซอร์ได้ฟรี ไม่ต้องติดตั้งอะไรในเครื่อง เหมาะสำหรับการฝึกปฏิบัติเบื้องต้น</p><p><b>ลิงก์:</b> <a href="https://www.play-with-docker.com/">https://www.play-with-docker.com/</a></p>`
   * - **3. CI/CD ด้วย GitHub Actions**
     - GitHub Actions Documentation
     - :raw-html:`<p>เอกสารทางการของ GitHub Actions ซึ่งละเอียดและมีตัวอย่างการสร้าง Workflow สำหรับสถานการณ์ต่างๆ</p><p><b>ลิงก์:</b> <a href="https://docs.github.com/en/actions">https://docs.github.com/en/actions</a></p>`
   * -
     - Awesome GitHub Actions
     - :raw-html:`<p>แหล่งรวม Actions สำเร็จรูปและ Workflow ตัวอย่างมากมายจากชุมชน ช่วยให้เห็นไอเดียและนำไปปรับใช้ได้ง่ายขึ้น</p><p><b>ลิงก์:</b> <a href="https://github.com/sdras/awesome-actions">https://github.com/sdras/awesome-actions</a></p>`
   * - **4. Infrastructure as Code (IaC) ด้วย Ansible**
     - Ansible Documentation
     - :raw-html:`<p>เอกสารทางการของ Ansible ที่อธิบายตั้งแต่พื้นฐาน, การเขียน Playbook, Modules ต่างๆ ไปจนถึงการจัดการ Roles และ Vaults</p><p><b>ลิงก์:</b> <a href="https://docs.ansible.com/ansible/latest/index.html">https://docs.ansible.com/ansible/latest/index.html</a></p>`
   * -
     - Ansible Tutorials (Red Hat)
     - :raw-html:`<p>Red Hat (เจ้าของ Ansible) มีบทเรียนและ Lab ให้ทดลองทำ ช่วยให้เข้าใจการใช้งานจริงได้ดีขึ้น</p><p><b>ลิงก์:</b> <a href="https://www.ansible.com/resources/ansible-getting-started-labs-tutorials">https://www.ansible.com/resources/ansible-getting-started-labs-tutorials</a></p>`
   * - **5. Kubernetes และ Container Orchestration**
     - Kubernetes Documentation
     - :raw-html:`<p>เอกสารทางการของ Kubernetes ที่ครอบคลุมทุกแง่มุมของการใช้งาน K8s ตั้งแต่แนวคิดพื้นฐานไปจนถึงการจัดการ Cluster ที่ซับซ้อน</p><p><b>ลิงก์:</b> <a href="https://kubernetes.io/docs/home/">https://kubernetes.io/docs/home/</a></p>`
   * -
     - Kubernetes by Example (Red Hat)
     - :raw-html:`<p>บทเรียนพร้อมตัวอย่างโค้ดที่ช่วยให้เข้าใจ Components ต่างๆ ของ Kubernetes ได้ง่ายขึ้นผ่านการลงมือปฏิบัติจริง</p><p><b>ลิงก์:</b> <a href="https://developers.redhat.com/products/openshift/kubernetes-by-example">https://developers.redhat.com/products/openshift/kubernetes-by-example</a></p>`
   * -
     - Minikube Documentation
     - :raw-html:`<p>เอกสารสำหรับ Minikube ซึ่งเป็นเครื่องมือสร้าง Kubernetes cluster บนเครื่องส่วนตัว เหมาะสำหรับการเรียนรู้และพัฒนา</p><p><b>ลิงก์:</b> <a href="https://minikube.sigs.k8s.io/docs/">https://minikube.sigs.k8s.io/docs/</a></p>`
   * - **6. Monitoring และ Logging (Prometheus, Grafana)**
     - Prometheus Documentation
     - :raw-html:`<p>เอกสารทางการของ Prometheus อธิบายแนวคิด, การติดตั้ง, การตั้งค่า Alerting และ PromQL (ภาษาสำหรับ Query ข้อมูล)</p><p><b>ลิงก์:</b> <a href="https://prometheus.io/docs/">https://prometheus.io/docs/</a></p>`
   * -
     - Grafana Documentation
     - :raw-html:`<p>เอกสารทางการของ Grafana ครอบคลุมการสร้าง Dashboard, การเชื่อมต่อ Data Sources และการทำ Alerting</p><p><b>ลิงก์:</b> <a href="https://grafana.com/docs/grafana/latest/">https://grafana.com/docs/grafana/latest/</a></p>`

