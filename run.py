from app import app


def main(host='0.0.0.0', port='3007'):
    app.run(host=host, port=port)

if __name__ == '__main__':
    main()
