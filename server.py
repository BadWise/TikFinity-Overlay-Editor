#!/usr/bin/env python3
"""
Servidor HTTP simples para o overlay TikFinity
"""
import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Desabilitar cache para desenvolvimento
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        # Permitir uso em iframes
        self.send_header('X-Frame-Options', 'ALLOWALL')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        # Log customizado
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor do Overlay TikFinity rodando em http://{HOST}:{PORT}")
        print(f"📂 Servindo arquivos de: {os.getcwd()}")
        print(f"✨ Acesse index.html para começar")
        print(f"\n⚙️  Pressione Ctrl+C para parar o servidor\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor encerrado")
