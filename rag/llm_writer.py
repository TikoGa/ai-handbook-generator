from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class HFWriter:
    def __init__(self):
        model_name = "google/flan-t5-small"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def write_section(self, title: str, context: str) -> str:
        prompt = (
            f"Write a clear and structured textbook section titled '{title}'. "
            f"Use only the information provided.\n\n"
            f"Information:\n{context}\n"
        )

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            num_beams=4,
            repetition_penalty=1.5,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

        generated_text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return generated_text.strip()

