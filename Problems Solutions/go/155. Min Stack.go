package main

type MinStack struct {
    values []int
    mins []int
}


func getMin(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}


func CreateMinStack() MinStack {
    return MinStack{}
}


func (this *MinStack) Push(val int)  {
    this.values = append(this.values, val)

    if len(this.mins) == 0 {
        this.mins = append(this.mins, val)
    } else {
        this.mins = append(
            this.mins, 
            getMin(
                this.mins[len(this.mins) - 1], 
                this.values[len(this.values) - 1],
            ),
        )
    }
}


func (this *MinStack) Pop()  {
    this.values = this.values[:len(this.values) - 1]
    this.mins = this.mins[:len(this.mins) - 1]
}


func (this *MinStack) Top() int {
    return this.values[len(this.values) - 1]
}


func (this *MinStack) GetMin() int {
    return this.mins[len(this.mins) - 1]
}