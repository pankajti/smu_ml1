from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

# get the vector data from a random position
idx = np.random.randint(0, len(ds.target))
raw_row = ds.data[idx]  # as a vector
img = ds.data[idx].reshape((8, 8))  # reshaped to be an image

# custom plotting tools
gs = gridspec.GridSpec(4, 2)

plt.subplot(gs[0, :])  # show vector
plt.imshow(np.matrix(raw_row), cmap=plt.cm.bone, interpolation='nearest')
plt.title('Row vector')

plt.subplot(gs[1:, :])  # show image
plt.imshow(img, cmap=plt.cm.bone, interpolation='nearest')
plt.title('Vector reshaped as an 8x8 image')

plt.suptitle('Label is %d' % (ds.target[idx])) 