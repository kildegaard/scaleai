

# Prompt 1

I'm working on my graduation project (eCommerce), but I'm not familiar with JavaScript. My friend tried to help me with the shopping cart issue, but I did not understand anything in the code. He wrote the code in his language, and there are some unintelligible letters that I want to change to words so that I know what the code does. Also, add a comment before each function.
```
class SC {
  constructor(CID, PID, Q, PR) {
    this.CID = CID;
    this.PID = PID;
    this.Q = Q;
    this.PR = PR;
    this.totalPR = PR * Q;
    this.cid = SC.generate();
  }

  static generate() {
    return Math.floor(Math.random() * 1000000);
  }
}

class Product {
  constructor(PID, Q) {
    this.PID = PID;
    this.Q = Q;
  }
}

const products = [
  new Product(1, 100), 
];

const carts = [];

async function NC(cart, PID, CID, Q, PR) {
  if (!cart || PID <= 0 || CID <= 0 || PR <= 0 || Q <= 0) {
    throw new Error("Error Happened");
  }

  const existingProduct = products.find(p => p.PID === PID);
  if (!existingProduct) {
    throw new Error("Product not found");
  }

  const checkQ = existingProduct.Q - Q;
  if (checkQ < 0) {
    throw new Error("There is No Enough Q");
  }

  let cartItem = carts.find(c => c.PID === PID && c.CID === CID);
  if (cartItem) {
    cartItem.Q += Q;
    cartItem.totalPR = PR * cartItem.Q;
    existingProduct.Q = checkQ;
  } else {
    cartItem = new SC(CID, PID, Q, PR);
    carts.push(cartItem);
    existingProduct.Q = checkQ;
  }

  return true;
}

async function DELTEE(cid) {
  const cartIndex = carts.findIndex(c => c.cid === cid);
  if (cartIndex === -1) {
    throw new Error("Cart Not Found");
  }

  const cartItem = carts[cartIndex];
  const product = products.find(p => p.PID === cartItem.PID);
  if (!product) {
    throw new Error("No Products Found");
  }

  product.Q += cartItem.Q;
  carts.splice(cartIndex, 1);

  return true;
}


(async () => {
  try {
    await NC({}, 1, 1, 2, 10);
    console.log("Cart after adding:", carts);
    await DELTEE(carts[0].cid);
    console.log("Cart after deleting:", carts);
  } catch (error) {
    console.error(error.message);
  }
})();

```

# Justif 1

Both responses are almost the same. Both response compiles successfully, so no bug was added when generating the response. 
Both responses address what the prompt requires; they change all the one letter variable names to understandable words to make the code more readable. Also, both responses added comments before each function.
Response 1 is hardly better than Response 2 because explains what did it.

Both responses can be executed using the Sphere engine with no issues. Just copy, paste and run.


# Prompt 2

Now that I understand the idea and how each function works, I want you to add item prices as a database array and a function that edits the shopping cart. Display more than carts with prices.
Also, give an example of how the modified code will be executed step by step.


# Justif 2 orig

Both responses are the same.
The responses added the function of editing the shopping carts, prices, and items, and an explanation of how to execute them step by step as the prompt required. 
Also, both responses displayed examples of the editing cart shopping.

# Justif 2 modif

Both responses are the same. The responses added the function of editing the shopping carts, prices, and items, and an explanation of how to execute them step by step as the prompt required.
Despite this, there are some potential issues in both of them. For example, they both use `async` functions but never declare `await` codes. Also, the `cart` parameter is never used inside the `addNewItemToCart` function.
Once more, codes were locally tested with no problems.

