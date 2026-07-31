class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #matrix goes topleft then move that left til top right
        #move that top right til bottom right
        # move that bottom right til bottom left
        #move the bottom left until next val is the top left and change
        #top left to be the current top left val and same thing with rest

        output = []
        #when its just matrix[n] thats col
        left, right = 0, len(matrix[0])
        #just doing len(matrix) returns rows
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #first go left -> right to get every i in top row
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1  
            #get every value from top right to bottom right

            for i in range(top, bottom):
                output.append(matrix[i][right - 1]) 
            right -= 1

            if not(left < right and top < bottom):
                break

            #get every value from bottom right to bottom left
            for i in range(right - 1, left -1, -1):
                output.append(matrix[bottom-1][i])
            bottom -= 1

            #get bottom left to top left
            for i in range(bottom-1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        return output
        



            