from koradctl.cli import Cli

if __name__ == '__main__':
    try:
        cli = Cli()
        cli.run()
    except KeyboardInterrupt:
        pass
