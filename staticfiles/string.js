let value;

const firstname = "Louis"
const lastname = "Armstrong"

value = firstname + lastname;
value = firstname + " " + lastname;

value = "ahmet hamdi";

//value = value + " " + "tanpınar"

value += " tanpınar"

value = firstname.length;

value = firstname.concat(" ",lastname," ","Caz")

value = firstname.toLowerCase();

value = firstname.toUpperCase();

value = firstname[0];
value = firstname[4];
value = firstname[firstname.length - 1]

// index of
value = firstname.indexOf("L")
value = firstname.indexOf("o")

// char At
value = firstname.charAt(4)

// split
langs = "Java,Python,Javascript,Css"
value = langs.split(",")

// replace
value = langs.replace("Python","Ruby")

// includes
value = langs.includes("Java")
value = langs.includes("safasfasagas")

console.log(value)