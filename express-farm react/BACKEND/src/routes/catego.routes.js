import {Router} from 'express';
import { createCatego, getCatego, getCategoById, deleteCatego, updateCatego} from '../controllers/catego.controller.js'
import { authRequired } from '../middlewares/validateToken.js'
import { validateSchema } from '../middlewares/vaidator.middleware.js'
import { createCategoSchema } from '../schemas/catego.schema.js'
const router = Router();


router.post("/catego", authRequired, validateSchema(createCategoSchema), createCatego);
router.get("/catego", authRequired, getCatego);
router.get("/catego/:id", authRequired, getCategoById);
router.delete("/catego/:id", authRequired, deleteCatego);
router.put("/catego/:id", authRequired, updateCatego);
export default router;