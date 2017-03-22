from server.server_rpc import server_rpc

if __name__ == "__main__":
    server_rpc.start()
    server_rpc.wait()
