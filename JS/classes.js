class User{
    constructor(fname,lname){
        this.fname = fname;
        this.lname = lname;
    }

    printName(){
        console.log(this.fname + " " + this.lname);
    }
}

student = new User("Rohith","Kumar");
// console.log(student)
student.printName()