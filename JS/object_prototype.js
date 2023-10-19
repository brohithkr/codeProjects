
// prototype object oriented programming in js and prototypal inheritance
function User(fname,lname){
    User.prototype.species = "Homo Sapians"
    this.fname = fname;
    this.lname = lname;
    User.prototype.printName = function(){
        console.log(this.fname + " " + this.lname);
    };
}

let student = new User("Rohith","Kumar");

student.printName()
console.log(User.prototype.printName == student.printName)
console.log(student.__proto__)