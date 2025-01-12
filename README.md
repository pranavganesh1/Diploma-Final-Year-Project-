# 🔒 Cloud-Based Encryption and Decryption

This project was developed as part of my final year diploma in Computer Science. It focuses on implementing a cloud-based encryption and decryption system using **Amazon Web Services (AWS)**. The system securely encrypts data, and authorized users can decrypt it when needed, leveraging cloud resources to ensure scalability and efficiency.

---

## ✨ Features
- ✅ **Secure encryption of data** using cloud-based infrastructure.
- ✅ **Decryption functionality** for retrieving original data.
- ✅ **Hosted on an AWS EC2 instance.**
- ✅ **User-friendly process** for deploying and running the project.

---

## 🛠️ Technologies Used
- ☁️ **Amazon Web Services (AWS):** Cloud hosting.
- 🐍 **Python:** Programming language for encryption and decryption logic.
- 🔑 **PuTTY:** SSH client for connecting to the AWS instance.
- 🖥️ **Amazon Linux:** Operating system for the server instance.

---

## 📦 Prerequisites
Before starting, ensure you have the following:
- 🆔 An **AWS account**.
- 🔑 **PuTTY** installed on your system.
- 📖 Basic knowledge of working with **AWS and Python**.

---

## 🚀 Steps to Deploy and Run the Project

### Step 1: Launching an AWS EC2 Instance
1. Log in to your **AWS Management Console**.
2. Navigate to **EC2** and click on **Launch Instance**.
   ![EC2 Launch Instance](https://github.com/user-attachments/assets/cfbf23d1-d7c8-4e16-99f2-29cc852d02d0)
3. Provide a name for your instance and ensure **Amazon Linux** and the **Amazon Machine Image (AMI)** are selected.
   ![Select AMI](https://github.com/user-attachments/assets/d3ccef4b-033f-414b-a318-c100b8ee2e24)
4. Create or choose a **Key Pair**:
   ![Key Pair](https://github.com/user-attachments/assets/1ccc016f-64f3-4873-a0f8-50e9dbd7edb6)
   - If creating a new key pair, provide a name and select the `.ppk` option for **PuTTY**.
   ![PPK Selection](https://github.com/user-attachments/assets/62bd2de6-71ed-47d2-bc06-4de21237deef)
5. Configure a **Security Group** or create a new one for your instance.
   ![Security Group](https://github.com/user-attachments/assets/301385aa-bbcf-40bc-91d5-45e0d99cc5fd)
6. Click on **Launch Instance** and wait for it to initialize.
   ![Instance Launch](https://github.com/user-attachments/assets/95130c92-e78e-4dcf-8062-53c450a923d2)
7. Once the instance is ready, note or copy the **IPv4 address**.
   ![IPv4 Address](https://github.com/user-attachments/assets/1664ec1d-909c-4188-a481-55463c5d01bc)

---

### Step 2: Connecting to the EC2 Instance
1. Open the **PuTTY** application on your system.
2. In the PuTTY configuration window:
   - Enter the **Host Name** as `ec2-user@IP Address`.
   ![PuTTY Host Name](https://github.com/user-attachments/assets/3340424e-6cdb-45e1-85aa-936795412f65)
   - Expand **SSH** and then **Auth** in the left menu.
   - Under **Credentials**, browse and select the Key Pair you created earlier.
   ![Select Key Pair](https://github.com/user-attachments/assets/4abd1671-40df-47d8-8bf8-02469e5cdcb3)
3. Click on **Open** to establish the connection.
4. Accept any permission prompts to open the **Amazon Linux terminal**.

---

### Step 3: Setting Up the Project on EC2
1. Switch to the root user:
   ```bash
   sudo su -
   ```
2. Install **Python** and **pip**:
   ```bash
   yum install python3-pip
   ```
3. Install the required libraries:
   ```bash
   pip install pycryptodome flask
   ```
4. Create a directory for the project:
   ```bash
   mkdir Dip-proj
   cd Dip-proj
   ```
5. Create a Python file using the `vi` editor:
   ```bash
   vi main.py
   ```
6. Press `i` to insert code and paste your encryption code using `Shift + Insert`.
7. Press `Esc`, type `:wq`, and press `Enter` to save and exit.
8. Run the script:
   ```bash
   python3 main.py
   ```

---

### Step 4: Testing the Encryption and Decryption
1. Copy the **IPv4 address** of your instance.
2. Open a web browser and paste the URL:
   ```
   http://[IP Address]/hello
   ```
3. The encrypted message will be displayed.
   ![Encrypted Message](https://github.com/user-attachments/assets/fa16248e-4ad7-44f2-980a-87a241759854)
4. For decryption:
   - Open the decryption script in **VS Code** or another Python IDE.
   - Use the same URL to test the decryption logic.
   ![Decryption](https://github.com/user-attachments/assets/fc7c2674-8ead-4d47-81ae-46dc8cd6a378)

---

## 📊 Project Use Cases
- 🔐 **Secure communication** over cloud-hosted systems.
- 🔑 **Data protection** for sensitive information using encryption.
- 🌐 **Cloud-based deployment** for scalable encryption services.

---

## 🤝 Contributions
Feel free to contribute to this project by:
- Suggesting improvements.
- Enhancing the encryption and decryption algorithms.
- Adding support for additional cloud platforms.

---

## 📜 License
This project is licensed under the **MIT License**.

