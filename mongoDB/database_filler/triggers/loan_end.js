exports = async function() {
  mongodb = context.services.get("AK7PD")
  loans_coll = mongodb.db("AK7PD").collection("loans")
  books_coll = mongodb.db("AK7PD").collection("books");
  users_coll = mongodb.db("AK7PD").collection("users");
  
  loans = await loans_coll.find({}).toArray().then(items => { return items}).catch(err => console.error(`Failed to find documents: ${err}`))
  
  loans.forEach(function(doc){
    ended = doc.hasOwnProperty('endDate')
    if(!ended){
      const dueDate = doc.dueDate
      const actualTime = new Date().getTime()
      if(dueDate < actualTime){
        updatedDocument = { ...doc, endDate: actualTime}
        str = JSON.stringify(updatedDocument, null, 4); // (Optional) beautiful indented output.
        console.log(str);
        books_coll.updateOne({_id: updatedDocument.book},{$inc: {"countAvailable": 1}})
        users_coll.updateOne({_id: updatedDocument.user},{$inc: {"loanCount": -1}})
        loans_coll.updateOne({_id: updatedDocument._id}, {$set: updatedDocument})
      }
    }
  })
  return 0
}
