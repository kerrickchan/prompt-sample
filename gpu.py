import torch
print(torch.backends.mps.is_available())
print(torch.backends.mps.is_macos13_or_newer())
# torch.cuda.is_available()
# #True
# torch.cuda.device_count()
# #1
# torch.cuda.current_device()
# #0
# torch.cuda.get_device_name(0)
# #'GeForce GTX 1080'
