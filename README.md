# TLS Validator
This tool simply checks TLS certificates from a list of domain names to see if they are valid.

This tool checks certificates for:
* If the certificate has expired
* If the certificate will expire in a number of days
* If the certificate and domain name do not match 
* If the certificate is not yet valid 

# Getting Started

## Creating the domain list
The list should be a simple text file with one domain name for each line.
Domain names should be names only, the protocol (https) is not needed.

example:
```
github.com
google.com
accounts.yahoo.com 
```

If you need to specify a port, it should be specified as such:
```
domain.com:port
```

## Setting up your Virtual Environment 
Create the virtual environment:
```
python -m venv env
```

(linux/mac) Activating your virtual environment:
```
. env/bin/activate
```

(windows) Activating your virtual environment:
```
env\Scripts\Activate
```

Install requirements:
```
pip install -r requirements.txt
```

## Running
Running main.py will begin the scanning process. If you created a domain list file you can include that filename as a paramater.
```
python main.py sample-file.txt
```
main.py will output two files in the `output` directory by default:

**all_domains.html**
* Contains all domains and their detected status.

**troubles.html**
* Contains ONLY domains that had issues detected.

You can modify these filenames in main.py

## Runing in Docker
Build the image:
```
docker build -t tls .
```
Run the image: (Be sure to swap out your filenames)
```
docker run -it --rm -v $(pwd)/sample-file.txt:/app/samplefile.txt -v $(pwd)/output:/app/output -eFILENAME=/app/sample-file.txt tls
```