# CUC-APIs

This is A sample to be used to automate some Rest APIs for Cisco CUC.

It can be used to add users, Delete Users And import User templated from CUC

Example:-

First assign CUC main Info 

CUC(UserName,Password,CUC_IP)

getVMts=cuc.Get_Templates() ##It could return list or dict

AddUser=CUC.Add_User(UserID,Extension,UserTemplate)
