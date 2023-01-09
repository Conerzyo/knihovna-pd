exports = function(changeEvent) {
  mongodb = context.services.get("AK7PD")
  loans_coll = mongodb.db("AK7PD").collection("loans")
  books_coll = mongodb.db("AK7PD").collection("books")
  users_coll = mongodb.db("AK7PD").collection("users")

  const loan_date = new Date().getTime()
  const due_date = loan_date + 300//518400
  var fullDocument = changeEvent.fullDocument;
  fullDocument = { ...fullDocument, loanDate: loan_date, dueDate: due_date}
  loans_coll.updateOne({_id: fullDocument._id}, {$set: fullDocument})
  books_coll.updateOne({_id: fullDocument.book},{$inc: {"countAvailable": -1}})
  users_coll.updateOne({_id: fullDocument.user},{$inc: {"loanCount": 1}})
};
