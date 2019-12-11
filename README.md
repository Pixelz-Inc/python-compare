# python-compare
A simple utility to compare two python objects. It does not abide by the python zen and notably makes use of private methods
- `__dict__`
- `__len__`
- `__getitem__`

for purposes for which these functions were not intended.

But it does the job of being pretty generic. It was initially made to compare Pytorch datasets which do not have a built in comparison function. The trick used to `# speedup string comparison` should also be used to speed up Tensor comparison and could probably be made even more generic by allowing the user to pass a list of classes for which equality can be directly tested.

The protection against infinite recusive loops is not fool proof either since it only only check the previous iteration. There could be loop with a cycle length greater than 1.

As you can see there is still a lot of `print` for debugging. It was intentionally left for helping with future improvements.

It is not in use at Pixelz any more but feel free to open issues and pull requests to improve it as needed.
