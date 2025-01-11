# Cloud-Based Encryption and Decryption

This project was developed as part of my final year diploma in Computer Science. It focuses on implementing a cloud-based encryption and decryption system using Amazon Web Services (AWS). The system securely encrypts data, and authorized users can decrypt it when needed, leveraging cloud resources to ensure scalability and efficiency.

## Features
- **Secure encryption of data** using cloud-based infrastructure.
- **Decryption functionality** for retrieving original data.
- **Hosted on an AWS EC2 instance.**
- **User-friendly process** for deploying and running the project.

## Technologies Used
- **Amazon Web Services (AWS):** Cloud hosting.
- **Python:** Programming language for encryption and decryption logic.
- **PuTTY:** SSH client for connecting to the AWS instance.
- **Amazon Linux:** Operating system for the server instance.

## Prerequisites
Before starting, ensure you have the following:
- An **AWS account**.
- **PuTTY** installed on your system.
- Basic knowledge of working with **AWS and Python**.

## Steps to Deploy and Run the Project

### Step 1: Launching an AWS EC2 Instance
1. Log in to your AWS Management Console.
2. Navigate to **EC2** and click on **Launch Instance**.
3. Provide a name for your instance and ensure **Amazon Linux** and the **Amazon Machine Image (AMI)** are selected.
4. Create or choose a Key Pair:
   - If creating a new key pair, provide a name and select the `.ppk` option for PuTTY.
5. Configure a **Security Group** or create a new one for your instance.
6. Click on **Launch Instance** and wait for it to initialize.
7. Once the instance is ready, note or copy the **IPv4 address**.

### Step 2: Connecting to the EC2 Instance
1. Open the **PuTTY** application on your system.
2. In the PuTTY configuration window:
   - Enter the **Host Name** as `ec2-user@IP Address`.
   - Expand **SSH** and then **Auth** in the left menu.
   - Under **Credentials**, browse and select the Key Pair you created earlier.
3. Click on **Open** to establish the connection.
4. Accept any permission prompts to open the **Amazon Linux terminal**.

### Step 3: Setting Up the Project on EC2
1. Switch to the root user:
   ```bash
   sudo su -
   ```
2. Install Python and pip:
   ```bash
   yum install python3-pip
   ```
3. Create a directory for the project:
   ```bash
   mkdir Dip-proj
   ```
4. Navigate to the directory:
   ```bash
   cd Dip-proj
   ```
5. Create a Python file using the `vi` editor:
   ```bash
   vi main.py
   ```
6. Press `i` to insert code.
7. Paste your encryption code using `Shift + Insert`.
8. Press `Esc`, type `:wq`, and press `Enter` to save and exit.
9. Run the script:
   ```bash
   python3 main.py
   ```

### Step 4: Testing the Encryption and Decryption
1. Copy the **IPv4 address** of your instance.
2. Open any web browser and paste the URL:
   ```
   IP Address/hello
   ```
3. You will see the encrypted message displayed.
4. For decryption:
   - Open the decryption script in **VS Code** or another Python IDE.
   - Use the same URL to test the decryption logic.

## Project Use Cases
- **Secure communication** over cloud-hosted systems.
- **Data protection** for sensitive information using encryption.
- **Cloud-based deployment** for scalable encryption services.

## Contributions
Feel free to contribute to this project by:
- Suggesting improvements.
- Enhancing the encryption and decryption algorithms.
- Adding support for additional cloud platforms.

## License
This project is licensed under the **MIT License**.

