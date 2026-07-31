class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #right is number of cols - 1
        l, r = 0, len(matrix[0]) -1
        
        while l < r:
            #basically we just want to rotate the amount of n we have in an nxn matrix and we get that by subtracting the right index from left
            for i in range(r - l):
                #do this counterclockwise even though we are rotating clockwise 
                top, bottom = l, r

                #save the topleft val
                #we also want to increment with i so it does every square from top n amount of squares [][][][] if n is 4
                topLeft = matrix[top][l + i]

                #move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #move topLeft to top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1
            #no need to update top and bottom b/c they get set to l,r in loop anyways
    #because this is IN place there is no need to return.