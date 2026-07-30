class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1 #points to the bottom row value
        left = 0
        right = len(matrix[0])-1 #points to the right most value

        result = [] #empty list to append to 
    
        while top <= bottom and left <= right: #edge case (?)
            #moves left to right first
            for c in range(left, right+1): #right + 1 because it stops BEFORE right
                result.append(matrix[top][c])
            top += 1 #move the top to the next row 

            #moves top to bottom
            for r in range(top, bottom+1):
                result.append(matrix[r][right])
            right -= 1

            #check because prev 2 changed the values of top and right
            #if there was one row top and bottom point to same but top is incremented so
            #it won't unnecessarily run this 
            if top <= bottom:
                #moves right to left
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom -=1
            #same for left right since its getting incremented once already
            if left <= right:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                left +=1

        return result