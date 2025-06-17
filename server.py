from livereload import Server

server = Server()

server.watch('index.html')
server.watch('style.css')

server.serve(root='.')
