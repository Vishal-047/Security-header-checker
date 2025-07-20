# Security Header Checker

A modern web application that analyzes website security headers and HTTPS configuration. Built with Flask and featuring a beautiful, responsive UI.

## Features

- 🔒 **HTTPS Status Check**: Verify if a website uses HTTPS for secure communication
- 🛡️ **Security Headers Analysis**: Check for important security headers including:
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection
  - Referrer-Policy
  - Permissions-Policy
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Real-time Analysis**: Instant results with loading indicators
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations

## Screenshots

The application features a clean, modern interface with:
- Gradient background and card-based layout
- Interactive buttons with hover effects
- Color-coded status indicators
- Responsive tables for header analysis
- Loading spinners and error handling

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter a website URL in the input field (e.g., `google.com` or `https://example.com`)
2. Click "Check Security" or press Enter
3. View the results:
   - **HTTPS Status**: Shows whether the site uses HTTPS
   - **Security Headers**: Detailed analysis of security headers with descriptions

## Security Headers Explained

- **Content-Security-Policy**: Prevents XSS attacks by controlling resource loading
- **Strict-Transport-Security**: Forces HTTPS connections
- **X-Content-Type-Options**: Prevents MIME type sniffing
- **X-Frame-Options**: Prevents clickjacking attacks
- **X-XSS-Protection**: Enables XSS filtering in browsers
- **Referrer-Policy**: Controls referrer information
- **Permissions-Policy**: Controls browser features and APIs

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome
- **HTTP Requests**: Python requests library
- **Data Format**: JSON API responses

## File Structure

```
cyber/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Main HTML template
```

## API Endpoints

- `GET /`: Main page
- `POST /check`: Security analysis endpoint
  - Request: `{"url": "example.com"}`
  - Response: JSON with HTTPS and headers analysis

## Error Handling

The application handles various error scenarios:
- Invalid URLs
- Connection timeouts
- Network errors
- Missing URLs

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Development

To run in development mode:
```bash
python app.py
```

The application will be available at `http://localhost:5000` with debug mode enabled.

## Security Notes

- This tool only performs passive analysis
- No data is stored or logged
- All requests are made from the server to the target website
- Use responsibly and only on websites you own or have permission to test

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 