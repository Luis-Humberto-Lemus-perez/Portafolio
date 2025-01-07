import {Router} from 'express';
import { newMedic,getMedicAll,getMedicById,deleteMedic,updateMedic,stockMedic} from '../controllers/medic.controller.js'
import { authRequired } from '../middlewares/validateToken.js'
import { validateSchema } from '../middlewares/vaidator.middleware.js'
import { createmedicSchema } from '../schemas/medic.schema.js'
const router = Router();


router.post("/medicine",authRequired, validateSchema(createmedicSchema), newMedic);
router.get("/medicine", getMedicAll);
router.get("/medicine/:id", authRequired, getMedicById);
router.delete("/medicine/:id", authRequired, deleteMedic);
router.put("/medicine/:id", authRequired, updateMedic);
router.put("/stock/:id", authRequired, stockMedic);
export default router;