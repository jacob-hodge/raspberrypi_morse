import React, { useState } from 'react';
import { Button, Form, Input } from 'semantic-ui-react';
export const TextForm = () => {
    const [message, setMessage] = useState('');
    
    return (
        <Form>
            <Form.Field>
                <Input placeholder= "enter message" value = {message} onChange={e => setMessage(e.target.value)} />
            </Form.Field>
            <Form.Field>
                <Button onClick={async () => {
                    console.log(message);
                    const response = await fetch('/api/run_led', {

                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(message)
                    })  
                    if (response.ok) {
                        console.log('response worked')
                    }
                }}>
                Send
                </Button>
            </Form.Field>
        </Form>
    )
}