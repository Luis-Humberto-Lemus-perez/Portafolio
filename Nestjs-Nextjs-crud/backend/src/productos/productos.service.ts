import { ConflictException, Injectable, InternalServerErrorException, NotFoundException} from '@nestjs/common';
import { CreateProductoDto } from './dto/create-producto.dto';
import { UpdateProductoDto } from './dto/update-producto.dto';
import { PrismaService } from 'src/prisma/prisma.service';
import { Prisma } from '@prisma/client';

@Injectable()
export class ProductosService {

  constructor(private prismaService: PrismaService) {
    
  }
  async create(createProductoDto: CreateProductoDto) {
    try {
      return await this.prismaService.product.create({
        data: createProductoDto
      })
      
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError){
        if (error.code === 'P2002'){
          throw new ConflictException('There is a product with the same name')
        }
      
      }
   
    }
    throw new InternalServerErrorException()
  }

  findAll() {
     return this.prismaService.product.findMany()
   
  }

  async findOne(id: number) {
    const productFound= await this.prismaService.product.findUnique({
      where: {id: id}
    })
    if(!productFound){
      throw new NotFoundException('Product whint id ${id} not found')
    }
    
    return productFound
   
  }

  async update(id: number, updateProductoDto: UpdateProductoDto) {
    const productFound=  await this.prismaService.product.update({
      where: {id: id},
      data: updateProductoDto

    })
    if (!productFound){
      throw new NotFoundException('Product whint id ${id} not found')
    }
    return productFound
  }

  async remove(id: number) {
    const deletepProduct= await this.prismaService.product.delete({
      where: {id: id}
    })
    if(!deletepProduct){
      throw new NotFoundException('Product whint id ${id} not found')
    }
    return deletepProduct
  }
}
