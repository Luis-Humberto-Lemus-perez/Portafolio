import Medic from "../models/medic.model.js";

export const newMedic = async (req, res) => {
  const { name, description, img, precio, stock, category} = req.body;
    try {
      const medicFound = await Medic.findOne({ name})
      console.log(req.user);
      if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
      if (medicFound) 
      return res.status(400).json({message:"Medicine already exists"});

      
     
      const medicUser = new Medic({
        name,
        description,
        img,
        precio,
        stock,
        category,
      
      });
      const medicSaved = await medicUser.save();
      
      res.json({
        id:  medicSaved._id,
          name: medicSaved.username,
          description: medicSaved.description,
          img: medicSaved.img,
          precio: medicSaved.precio,
          stock: medicSaved.stock,
          category: medicSaved.category,
          createdAt: medicSaved.createdAt,
          updatedAt: medicSaved.updatedAt
      });
    } catch (error) {
      console.error("Error registering medicine: ", error);
    }
};

export const getMedicAll = async (req, res) => {
  try {
   
      const medic = await Medic.find({});
      res.json(medic);
    
  } catch (error) {
    console.error("Error getting medicine: ", error);
  }
};

export const getMedicById = async (req, res) => {
  try {
    if (req.user.role === "user")
      return res.status(403).json({ message: "Unauthorized" });
    const medicine = await Medic.findById(req.params.id);
    if (!medicine)
      return res.status(404).json({ message: "medicine not found" });
    res.json(medicine);
  } catch (error) {
    return res.status(500).json({ message: "Error getting medicine" });
  }
};
export const deleteMedic = async (req, res) => {
  try {
    if (req.user.role === "user")
      return res.status(403).json({ message: "Unauthorized" });
    const medicine = await Medic.findByIdAndDelete(req.params.id);
    if (!medicine)
      return res.status(404).json({ message: "medicine not found" });
    return res.sendStatus(204);
  } catch (error) {
    return res.status(500).json({ message: "Error deleting medicine" });
  }
};
export const updateMedic = async (req, res) => {
  try {
    if (req.user.role === "user")
      return res.status(403).json({ message: "Unauthorized" });
    const medicene = await Medic.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!medicene)
      return res.status(404).json({ message: "medicene not found" });
    res.json(medicene);
  } catch (error) {
    return res.status(500).json({ message: "Error updating medicene" });
  }
};
export const stockMedic = async (req, res) => {
  try {
    if (req.user.role === "user") {
      const medicineid = await Medic.findById(req.params.id);
      if (!medicineid)return res.status(404).json({ message: "medicine not found" });
        console.log(req.body);
      const shop = medicineid.stock - req.body.stock;
        console.log(shop);
      if (shop < 0)return res.status(400).json({ message: "No stock available" });
        req.body = { stock: shop }
      const medicene = await Medic.findByIdAndUpdate(req.params.id, req.body, {
        new: true,
      });
      if (!medicene)
        return res.status(404).json({ message: "medicene not found" });
      res.json(medicene);
    }
  } catch (error) {
    return res.status(500).json({ message: "Error updating medicene" });
  }
};
