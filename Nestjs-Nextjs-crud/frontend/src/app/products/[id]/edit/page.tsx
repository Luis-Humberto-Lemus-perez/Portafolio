

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import * as React from 'react'

import {ProductForm} from './edit-form'
import { getProduct } from '../../products.api'
import Link from 'next/link'
import { buttonVariants } from '@/components/ui/button'



async function ProductsEditPage ({params}) {
   const { id } = await params
    console.log(id)
    const product = await getProduct(id);
    
  return (
    <div className='h-screen flex justify-center items-center'>
        <Card>
            <CardHeader>
                <CardTitle>
                Create Product
                <Link
                    className={buttonVariants()}
                    href="/"
                >
                    Go back
                </Link>
                </CardTitle>
            </CardHeader>
            <CardContent>
                <ProductForm product={product} />
            </CardContent>
        </Card>

    </div>
  )
}

export default ProductsEditPage