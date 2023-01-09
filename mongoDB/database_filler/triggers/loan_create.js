exports = function(changeEvent) {
  mongodb = context.services.get("AK7PD")
  console.log(mongodb)
  collection = mongodb.db("AK7PD").collection("loans")

  const loan_date = Math.floor(Date.now() / 1000)
  const due_date = loan_date + 518400
  var fullDocument = changeEvent.fullDocument;
  fullDocument = { ...fullDocument, loanDate: loan_date, dueDate: due_date}
  collection.insertOne(fullDocument)
};
