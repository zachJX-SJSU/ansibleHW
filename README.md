The entire project is deployed on 3 AWS EC2 ubuntu instances: one control node that hosts the Ansible playbook and Flask project source code; two managed VMs that actually deploys the Flask program.
### H3 Web App:
 The web page is written using Python Flask. The app listens on port 8080, and the webpage will display a text "Hello from SJSU-{VAR}" where "VAR" is an environmental parameter set up Ansible.

### H3 Ansible playbook:
  Use Ansible's built-in copy to deploy source code from control node to managed node. See "ansible_cmd.txt" for deploy/undeploy the web app.
