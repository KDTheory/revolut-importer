# FireflyRevolutTransactions

Automatic import of Revolut transactions into FireflyIII personal finance manager, 
made with use of [revolut-python](https://github.com/tducret/revolut-python).

## Usage
During the first run it gets hash of last transaction, without any import into FireflyIII, 
which is stored in user's cache folder. This transaction is later used as a base from which it will start importing,
and is updated on subsequent runs to avoid duplicating of transactions.

```
Usage: firefly_revolut_cli.py [OPTIONS]

Options:
  -r, --revolut-token TEXT  Revolut token (required)
  -f, --firefly-token TEXT  Firefly token (required)
  -a, --account-id TEXT     Id of Revolut account in FireflyIII (required)
  -v, --vault-id TEXT       Id of Revolut vault in FireflyIII
  -t, --topup-id TEXT       Id of topup account in FireflyIII
  -u, --firefly-url TEXT    URL to FireflyIII instance including trailing
                            slash "/" (required)
  --help                    Show this message and exit.
```

It is recommended to use [FireflyIII Rules](https://docs.firefly-iii.org/advanced-concepts/rules)
to adjust transactions as they get imported to your individual needs.

## Getting Revolut token

Use [revolut-python](https://github.com/tducret/revolut-python) client to receive the Revolut token.

## Getting FireflyIII token

Use [Personal Access Token](https://docs.firefly-iii.org/api/api) in your FireflyIII instance Profile menu.

