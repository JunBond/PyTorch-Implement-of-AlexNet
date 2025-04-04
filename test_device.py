import torch

flag = torch.cuda.is_available()
print(flag)
ngpu = 1

device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu >0) else "cpu")
print("Using device:",device)
print(torch.cuda.get_device_name(0))
print(torch.rand(3,3).cuda)

cuda_version = torch.version.cuda
print("CUDA Version:", cuda_version)

cudnn_version = torch.backends.cudnn.version()
print("CuDNN Version:",cudnn_version)
