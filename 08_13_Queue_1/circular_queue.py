Q_SIZE =4
cQ = [0]
front= rear=0

rear = (rear+1)%Q_SIZE  # enq(1)
cQ[rear]=1

rear = (rear+1)%Q_SIZE  # enq(2)
cQ[rear]=2

rear = (rear+1)%Q_SIZE  # enq(3)
cQ[rear]=3
