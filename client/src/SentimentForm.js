import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";
export const SentimentForm = () => {
    const [sentence, setSentence] = useState('');

    return (
        <Form>
            <Form.Field>
                <Input 
                placeholder="My sentence" 
                value={sentence} 
                onChange={e => setSentence(e.target.value)}/>
            </Form.Field>
            <Form.Field>
                <Button onClick={async () => {
                    const my_sentence = {sentence}
                    const response = await fetch('/model', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(my_sentence)
                    })
                    if (response.ok) {
                        console.log("response work!")
                    }
                }}>Submit</Button>
            </Form.Field>
        </Form>
    )


}