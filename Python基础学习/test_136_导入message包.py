import test_message

test_message.send_message.send("hello")
txt = test_message.receive_message.receive()
print(txt)
