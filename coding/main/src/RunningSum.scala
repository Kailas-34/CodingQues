package main.src

object RunningSum {

  def main(args: Array[String]): Unit = {

    var nums = Array[Int](1, 2, 3, 4)

    for (element <- runningSum(nums) ) { println(element)}

    def runningSum(nums: Array[Int]): Array[Int] = {
      var result = new Array[Int](nums.length)
      result(0) = nums(0)
      for (i <- 1 until nums.length ) {

        result(i) = result(i - 1) + nums(i)

      }

       result

    }

  }

}
