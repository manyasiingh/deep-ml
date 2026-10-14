import torch

def make_tensor():
    """Return a 2x3 float32 tensor [[1, 2, 3], [4, 5, 6]]."""
    tensord = torch.tensor([[1,2,3],[4,5,6]])
    tensorf = tensord.to(torch.float32)
    return tensorf
    pass
