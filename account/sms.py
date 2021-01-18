from twilio.rest import Client

account_sid ='ACe7f2f6757e927d7ed6d2c8c57c25da92'
auth_token ='51540d24f6e40868d2373693db805583'

client=Client(account_sid ,auth_token)

message=client.message/
    .create(
        body='Hey whatsapp here is your otp'
        from='+1923442'
        to=''
    )

def send_sms(account_sid,auth_token,body,from_,to_):
    from twilio.rest import Client
    client=Client(account_sid ,auth_token)
    message=client.message/
        .create(
            body=body,
            from =from_,
            to=to_
        )