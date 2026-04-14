# Campus Fire Safety Management System

## Project Structure

```plaintext
campus_fire/
├── backend/
│   ├── app/
│   │   ├── __init__.py               # Flask app initialization
│   │   ├── models.py                  # Database models
│   │   ├── routes.py                  # API routes
│   │   ├── auth.py                    # Authentication logic
│   │   ├── config.py                  # Configuration settings
│   │   └── requirements.txt           # Python dependencies
│   ├── Dockerfile                      # Docker configuration for Flask
│   └── docker-compose.yml              # Docker Compose setup
├── frontend/
│   ├── src/
│   │   ├── main.js                   # Entry file for Vue
│   │   ├── App.vue                    # Main component
│   │   └── components/                # Vue components
│   ├── public/                        # Public assets
│   ├── package.json                   # NPM dependencies
│   └── vite.config.js                 # Vite configuration
├── microprogram/
│   ├── app/                          # WeChat mini-program files
│   └── config.js                     # Mini-program configurations
├── database/
│   ├── schema.sql                     # MySQL schema
│   └── migrations/                    # Migration scripts
├── deployment/
│   ├── Alibaba_Cloud_Configuration.md # Alibaba Cloud setup instructions
│   ├── nginx.conf                     # Nginx configuration
│   └── deployment_guide.md            # General deployment guide
└── config/
    ├── config.yaml                   # Overall configuration file
    └── secrets.env                    # Environment secrets
```  

---

This file contains the base directory structure for the Campus Fire Safety Management System project. Each folder contains essential files for backend, frontend, microprogram, database, deployment, and configuration.