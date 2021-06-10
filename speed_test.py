import speedtest

Test_Speed = speedtest.Speedtest()

print("Loading server list... ")
Test_Speed.get_servers()

print("Choosing best server... \n")
Best_server = Test_Speed.get_best_server()
#print(Best_server)
print(f"Found: {Best_server['host']} located in {Best_server['country']} - {Best_server['name']} / CC: {Best_server['cc']} sponsor: {best['sponsor']}\n")



print("downloading Test... ")
download = Test_Speed.download()

print("uploading Test...\n ")
upload = Test_Speed.download()

ping_result = Test_Speed.results.ping

print(f"Download speed : {download / 1024 / 1024:.2f} Mbit/s ")
print(f"  upload speed : {upload / 1024 / 1024:.2f} Mbit/s")
print(f"          ping : {ping_result:.2f} ms")
input("press Enter To Exit: ")
