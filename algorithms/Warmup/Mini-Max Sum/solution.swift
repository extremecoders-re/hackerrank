import Foundation

// Complete the miniMaxSum function below.
func miniMaxSum(arr: [Int64]) -> Void {
    var min:Int64 = arr[0]
    var max:Int64 = arr[0]
    var sum:Int64 = 0
    
    for elem in arr {
        if elem > max {
            max = elem
        } 
        else if elem < min {
            min = elem
        }
        
        sum += elem
    }    
    print("\(sum-max) \(sum-min)")
}

guard let arrTemp = readLine() else { fatalError("Bad input") }
let arr: [Int64] = arrTemp.split(separator: " ").map {
    if let arrItem = Int64($0.trimmingCharacters(in: .whitespacesAndNewlines)) {
        return arrItem
    } else { fatalError("Bad input") }
}

guard arr.count == 5 else { fatalError("Bad input") }

miniMaxSum(arr: arr)
