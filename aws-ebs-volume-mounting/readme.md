AWS EBS Volume Mounting:

🔧 Step 1: Create an EBS Volume Go to the EC2 Dashboard in AWS Console. In the left panel, click Elastic Block Store > Volumes. Click Create Volume. Fill in: Size (e.g., 10 GiB) Availability Zone (Must match your EC2 instance) Leave other options default Click Create Volume.

🔗 Step 2: Attach Volume to EC2 Instance Select the newly created volume. Click Actions > Attach Volume. Choose your instance and device name (e.g., /dev/xvdf). Click Attach.

The volume status changes from Available ➝ In-use.

🧪 Step 3: Verify the Volume is Attached lsblk Output will show /dev/xvdf (or similar) listed without a mountpoint.

🧱 Step 4: Format the Volume with ext4 sudo mkfs -t ext4 /dev/xvdf or sudo mkfs.ext4 /dev/xvdf

❓ Why Do We Format the Volume? When you create a new EBS volume, it's like a brand-new hard drive — it has no filesystem. Formatting it is essential because:

It defines how data is stored and organized. It prepares the volume to store files and directories. It enables the system to mount and use the volume. ⚠️ Without formatting, the volume cannot be used to store any data.

📂 Step 5: Create a Mount Directory sudo su : to swtich to super user cd / : to go to home directory mkdir /your-dir-name : to create new directory Learn Linux commands from scratch

📌 Step 6: Mount the Volume mount /dev/xvdf /test

Verify the mount:

df -h 🔁 Step 7: Make the Mount Persistent (After Reboot) To make the mount persistent, add an entry to /etc/fstab.

First, get the UUID: blkid

Open the fstab file: vi /etc/fstab Note: press "i" to insert mode press "esc" to return press ":wq!" to write and exit

🔄 Step 8: Reboot and Verify reboot After reboot, connect again and run:

df -h You should see /test mounted. ✅

🧹 Optional: Test Persistence You can unmount and remount to test:

umount /test mount -a df -h
