

public class PizzaWahala{
    public static void main(String[]args){
        pizzaWahala (10, "Big Boys");




    }


    public static void pizzaWahala(int numberOfGuests, String typeOfGuests){

        int slices = 0;
        int price = 0;

        if (typeOfGuests.equalsIgnoreCase("Sapa Size")){
            slices = 4;
            price = 2000;

        }
         else if (typeOfGuests.equalsIgnoreCase("Small Money")){
            slices = 6;
            price = 2400;

        }
         else if (typeOfGuests.equalsIgnoreCase("Big Boys")){
            slices = 8;
            price = 3000;

        }
         else if (typeOfGuests.equalsIgnoreCase("Odogwu")){
            slices = 12;
            price = 4200;

        }
        else{
            System.out.println("Invalid Order");
            return;

        }
        
        int boxes = (numberOfGuests + slices -1) / slices;
        int totalPrice = boxes * price;
        int remainder = boxes * slices - numberOfGuests;


        System.out.println("Number of Boxes To Buy: " + boxes);
        System.out.println("The Remaining Slices: " + remainder);
        System.out.println("The Total price Is: " + totalPrice);

    



    }


}
