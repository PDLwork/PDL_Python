import torch

class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__() #用子类对象调用父类已被覆盖的方法 好像就是说将父类的优先级调高，可以参考菜鸟教程
    
    def forward(self, input):   #注意这个forward，换成别的函数名不行，其内部调用了__call__的方法,所以在下面可以直接使用
        output = input + 1
        return output

test = MyModel()
x = torch.tensor(1.0)
output = test(x)    #直接使用
print(output)