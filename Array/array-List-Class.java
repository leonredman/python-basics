class ArrayList {
   // Private members
   private int[] arrayData;
   private int arrayListLength;

   // The default constructor initializes the list with a capacity of 4
   public ArrayList() {
      this(4);
   }
   
   public ArrayList(int capacity) {
      this.arrayData = new int[capacity];
      this.arrayListLength = 0;
   }
}