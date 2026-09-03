from client import OperatorMultiStepTransactionFunnelOrchestratorClient

def main():
    client = OperatorMultiStepTransactionFunnelOrchestratorClient()
    res = client.orchestrate_checkout_funnel('chk_8812', ['CART_LOCK', 'ADDRESS_SELECT', 'CHARGE'])
    print('Operator Transaction Funnel Orchestrator: ' + res['orchestrator_run_id'] + ' (' + res['funnel_status'] + ')')
    print('Steps: ' + ' -> '.join(res['completed_steps']) + ' | Paid: ' + str(res['payment_token_dispatched']))
    print('Replay URL: ' + res['operator_audit_replay_url'])

if __name__ == '__main__':
    main()
