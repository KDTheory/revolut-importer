#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import sys

from firefly_revolut_transactions import FireflyRevolutClient


@click.command()
@click.option(
    '--revolut-token', '-r',
    envvar="REVOLUT_TOKEN",
    type=str,
    help='Revolut token (required)',
)
@click.option(
    '--firefly-token', '-f',
    envvar="FIREFLY_TOKEN",
    type=str,
    help='Firefly token (required)',
)
@click.option(
    '--account-id', '-a',
    envvar="REVOLUT_ACCOUNT",
    type=str,
    help='Id of Revolut account in FireflyIII (required)',
)
@click.option(
    '--vault-id', '-v',
    envvar="REVOLUT_VAULT",
    type=str,
    help='Id of Revolut vault in FireflyIII',
)
@click.option(
    '--topup-id', '-t',
    envvar="TOPUP_ACCOUNT",
    type=str,
    help='Id of topup account in FireflyIII',
)
@click.option(
    '--wallet-id', '-w',
    envvar="WALLET_ACCOUNT",
    type=str,
    help='Id of wallet account in FireflyIII',
)
@click.option(
    '--firefly-url', '-u',
    envvar="FIREFLY_URL",
    type=str,
    help='URL to FireflyIII instance including trailing slash "/" (required)',
)
def main(revolut_token, firefly_token, account_id, vault_id, topup_id, wallet_id, firefly_url):
    if revolut_token is None:
        print("You don't have a Revolut token. Use 'revolut_cli' to obtain one")
        sys.exit()
    if firefly_token is None:
        print("You don't have a FireflyIII token. Use 'Create Personal Access token' option in FireflyIII")
        sys.exit()
    if account_id is None:
        print("You don't have a Revolut account Id inside FireflyIII")
        sys.exit()
    if firefly_url is None:
        print("You don't have FireflyIII instance URL")
        sys.exit()

    client = FireflyRevolutClient(revolut_token, firefly_token, account_id, firefly_url, vault_id, topup_id, wallet_id)
    client.process()


if __name__ == "__main__":
    main()
