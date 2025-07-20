from flask import Flask, render_template, request, jsonify
import requests
from prettytable import PrettyTable
import io
import sys
import os

app = Flask(__name__)

def check_https(url):
    """Check if HTTPS is enabled for the given URL"""
    if url.startswith("https://"):
        return {"status": "success", "message": "✅ HTTPS is enabled."}
    else:
        return {"status": "warning", "message": "⚠ WARNING: HTTPS is NOT enabled. Use HTTPS for secure communication."}

def check_security_headers(url):
    """Check security headers for the given URL"""
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        security_headers = {
            'Content-Security-Policy': 'Prevents XSS attacks by controlling resource loading',
            'Strict-Transport-Security': 'Forces HTTPS connections',
            'X-Content-Type-Options': 'Prevents MIME type sniffing',
            'X-Frame-Options': 'Prevents clickjacking attacks',
            'X-XSS-Protection': 'Enables XSS filtering in browsers',
            'Referrer-Policy': 'Controls referrer information',
            'Permissions-Policy': 'Controls browser features and APIs',
        }

        results = []
        for header, description in security_headers.items():
            if header in headers:
                results.append({
                    "header": header,
                    "present": True,
                    "value": headers[header],
                    "description": description,
                    "status": "success"
                })
            else:
                results.append({
                    "header": header,
                    "present": False,
                    "value": "Missing",
                    "description": description,
                    "status": "warning"
                })

        return {"status": "success", "results": results}

    except requests.exceptions.Timeout:
        return {"status": "error", "message": "Request timed out. Please try again."}
    except requests.exceptions.ConnectionError:
        return {"status": "error", "message": "Connection error. Please check the URL and try again."}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({"status": "error", "message": "Please provide a URL"})
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Check HTTPS
    https_result = check_https(url)
    
    # Check security headers
    headers_result = check_security_headers(url)
    
    return jsonify({
        "https_check": https_result,
        "headers_check": headers_result,
        "url": url
    })

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 