import Catego from "../models/catego.model.js";
export const getCatego = async (req, res) => {
    try {
        if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
        const catego = await Catego.find({
        })
        res.json(catego);
      } catch (error) {
        console.error("Error getting catego: ", error);
      }
}
export const createCatego = async (req, res) => {
    const { name, description } = req.body;
    try {
      const categoFound = await Catego.findOne({ name})
      console.log(req.user);
      if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
      if (categoFound) 
      return res.status(400).json({message:"Category already exists"});

      
     
      const categoUser = new Catego({
        name,
        description,
      
      });
      const categoSaved = await categoUser.save();
      
      res.json({
        id:  categoSaved._id,
          name: categoSaved.username,
          description: categoSaved.description,
          createdAt: categoSaved.createdAt,
          updatedAt: categoSaved.updatedAt
      });
    } catch (error) {
      console.error("Error registering category: ", error);
    }
  };

export const getCategoById = async (req, res) => {
    try {
        if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
        const catego = await Catego.findById(req.params.id);
        if (!catego) return res.status(404).json({ message: "catego not found" });
        res.json(catego);
      } catch (error) {
        return res.status(500).json({ message: "Error getting catego" });
      }
}

export const deleteCatego = async (req, res) => {

    try {
        if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
        const catego = await Catego.findByIdAndDelete(req.params.id);
        if (!catego) return res.status(404).json({ message: "catego not found" });
        return res.sendStatus(204);
      } catch (error) {
        return res.status(500).json({ message: "Error deleting catego" });
      }
}
export const updateCatego = async (req, res) => {
    try {
        if (req.user.role === "user") return res.status(403).json({ message: "Unauthorized" });
        const catego = await Catego.findByIdAndUpdate(req.params.id, req.body, {
          new: true,
        });
        if (!catego) return res.status(404).json({ message: "catego not found" });
        res.json(catego);
      } catch (error) {
        return res.status(500).json({ message: "Error updating catego" });
      }
}