
import BRX, { BRK } from 'brx-node';
import { v_chat_ittr1 } from './schemas/brx_schema.mjs';

const brx = new BRX('brx15ebf1c0ec82781eb4569a4a2b638706004bf94615ff5b4262726e7df737e5ac', { verbose: false });

let brxObject = new BRK(v_chat_ittr1);

brxObject.input['input'].value = "ball";
brxObject.input['image_var'].value = "bitcoin"; //change only this parameter


const result = await brx.execute(brxObject, (event) => {
    console.log("Inline Event...")
    console.log(event)
});
console.log("Final Result...")
console.log(result)